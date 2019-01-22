import sys

cookiecutterVars = {
    'projectName': '{{cookiecutter.project_name}}',
    'RPATool': '{{cookiecutter.RPA_tool}}',
    'RPATaskName': '{{cookiecutter.RPA_task_name}}',
    'RPATaskExtension': '{{cookiecutter.RPA_task_extension}}',
    'RobotTaskFeatureDescription': '{{cookiecutter.Robot_task_feature_description}}'
}

# def commonError():
#     # print(f'ERROR: {cookiecutterVars["RPATool"]} not valid for {cookiecutterVars["RPATaskExtension"]}')
#     sys.stdout.write(f'ERROR: {cookiecutterVars["RPATool"]} not valid for {cookiecutterVars["RPATaskExtension"]}')
#     sys.exit(1)

# for key, value in cookiecutterVars.items():
#     if value == '':
#         print(f'ERROR: {key} = NULL is not a valid option')
#     sys.exit(1)

if cookiecutterVars['RPATool'] == 'AutomationAnywhere' and not cookiecutterVars['RPATaskExtension'] == '.atmx' :
    print(f'ERROR: {cookiecutterVars["RPATool"]} not valid for {cookiecutterVars["RPATaskExtension"]}')
    sys.exit(1)
elif cookiecutterVars['RPATool'] == 'UIPath' and not cookiecutterVars['RPATaskExtension'] == '.xaml' :
    print(f'ERROR: {cookiecutterVars["RPATool"]} not valid for {cookiecutterVars["RPATaskExtension"]}')
    sys.exit(1)
