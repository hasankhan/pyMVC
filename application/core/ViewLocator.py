from werkzeug.contrib.cache import SimpleCache
from flask import current_app as app
import os

class ViewLocator:
    __cache = SimpleCache()

    @staticmethod
    def __get_controller_name(controller):
        controller_name = controller.__class__.__name__
        if controller_name[-10:].lower() == 'controller':
            controller_name = controller_name[:-10]
        return controller_name
    
    @staticmethod    
    def __view_exists(controller, view_path):
        return os.path.isfile(os.path.join(app.template_folder, view_path))
        
    @staticmethod
    def __view_exists_in_dir(controller, base_dir, view_name):
        view_path = os.path.join(base_dir, view_name);
        return ViewLocator.__view_exists(controller, view_path)
        
    @staticmethod
    def __get_view_names(device, view_name):
        view_name, ext = os.path.splitext(view_name)
        ext = ext[1:] or 'html'
        
        names = []
        
        if device != '':
            names.append('{0}.{1}'.format(view_name, device))
            names.append('{0}.{1}.{2}'.format(view_name, device, ext))                    
        names.append(view_name)
        names.append('{0}.{1}'.format(view_name, ext))            
        
        return names
        
    @staticmethod
    def __find_view(controller, view_name):
        if view_name.find('/') == -1:                
            controller_name = ViewLocator.__get_controller_name(controller).lower()
            
            # first look for views/[controller_name]/[view_name]
            # otherwise look for views/Shared/view_name
            locations = [(controller_name, view_name), 
                        (controller_name, view_name.lower()),
                        ('Shared', view_name),
                        ('Shared', view_name.lower())]
                        
            for location in locations:                
                base_dir, name = location
                if ViewLocator.__view_exists_in_dir(controller, base_dir, name):                        
                    return '{0}/{1}'.format(base_dir, name)
            
        return view_name
        
    @staticmethod
    def resolve_view_name(controller, view_name):        
        device = controller.resolve_device_name()
        
        key = "{0}:{1}:{2}".format(controller.__class__.__name__, view_name, device)        
        view_path = ViewLocator.__cache.get(key)        
    
        if view_path is None:                
            names = ViewLocator.__get_view_names(device, view_name)                
            for name in names:
                view_path = ViewLocator.__find_view(controller, name)        
                if view_path != name:
                    break
                    
            ViewLocator.__cache.set(key, view_path)
        
        return view_path    
