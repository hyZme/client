## *********************************************************
## 
## File autogenerated for the dynamic_reconfigure_example package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'SUB', 'lower': 'sub', 'srcline': 123, 'name': 'Sub', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::SUB', 'field': 'DEFAULT::sub', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 11, 'description': 'small num test', 'max': 0.5, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/pi/catkin_ws_1/src/dynamic_reconfigure_tools/dynamic_reconfigure_example/cfg/Example.cfg', 'name': 'small_double', 'edit_method': '', 'default': 0.001, 'level': 1, 'min': 0.0, 'type': 'double'}, {'srcline': 12, 'description': 'big num test', 'max': 1500000000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/pi/catkin_ws_1/src/dynamic_reconfigure_tools/dynamic_reconfigure_example/cfg/Example.cfg', 'name': 'big_double', 'edit_method': '', 'default': 500000000.0, 'level': 1, 'min': 1000.0, 'type': 'double'}], 'type': '', 'id': 1}, {'upper': 'SUB2', 'lower': 'sub2', 'srcline': 123, 'name': 'Sub2', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::SUB2', 'field': 'DEFAULT::sub2', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 15, 'description': 'small num test', 'max': 0.5, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/pi/catkin_ws_1/src/dynamic_reconfigure_tools/dynamic_reconfigure_example/cfg/Example.cfg', 'name': 'small_double2', 'edit_method': '', 'default': 0.001, 'level': 1, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 2}], 'parameters': [{'srcline': 293, 'description': 'frame rate Hz', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'double_param', 'edit_method': '', 'default': 20.0, 'level': 1, 'min': 0.1, 'type': 'double'}, {'srcline': 293, 'description': 'integer', 'max': 256, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'int_param', 'edit_method': '', 'default': 50, 'level': 1, 'min': 1, 'type': 'int'}, {'srcline': 293, 'description': 'bool', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'bool_param', 'edit_method': '', 'default': False, 'level': 1, 'min': False, 'type': 'bool'}, {'srcline': 293, 'description': 'string', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'str_param', 'edit_method': '', 'default': 'test', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 293, 'description': 'string with long label', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'extra_long_test_name_str', 'edit_method': '', 'default': 'test', 'level': 1, 'min': '', 'type': 'str'}, {'srcline': 293, 'description': 'A size parameter which is edited via an enum', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'enum_param', 'edit_method': "{'enum_description': 'An enum to set size', 'enum': [{'srcline': 21, 'description': 'A small constant', 'srcfile': '/home/pi/catkin_ws_1/src/dynamic_reconfigure_tools/dynamic_reconfigure_example/cfg/Example.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Small'}, {'srcline': 22, 'description': 'A medium constant', 'srcfile': '/home/pi/catkin_ws_1/src/dynamic_reconfigure_tools/dynamic_reconfigure_example/cfg/Example.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Medium'}, {'srcline': 23, 'description': 'A large constant', 'srcfile': '/home/pi/catkin_ws_1/src/dynamic_reconfigure_tools/dynamic_reconfigure_example/cfg/Example.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Large'}, {'srcline': 24, 'description': 'An extra large constant', 'srcfile': '/home/pi/catkin_ws_1/src/dynamic_reconfigure_tools/dynamic_reconfigure_example/cfg/Example.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'ExtraLarge'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Example_Small = 0
Example_Medium = 1
Example_Large = 2
Example_ExtraLarge = 3
