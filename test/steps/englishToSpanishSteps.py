# import sys
# sys.path.append("..")
# from actor import Actor
# from tasks.customTasks import AsTranslation
# from tasks.customTasks import goToGoogleTranslate
# from tasks.customTasks import translate
# from userinterface.pages.googleMain import SEARCH_BUTTON
# from userinterface.pages.googleMain import SEARCH_INPUT_BAR
# from abilities.defaultAbilities import browseTheWeb
# from browersCons import FIREFOX,CHROME

# Juan=None

# @given(u'Juan is on Google Translate searching by {Keyword} and using the webbrowser {WebBrowser}')
# def step_impl(context,Keyword,WebBrowser):
#     global Juan

#     Juan=Actor(named='Juan')
#     #Juan.can(browseTheWeb,withBrowser=FIREFOX)
#     Juan.can(browseTheWeb)

#     Juan.wasAbleTo(
#         goToGoogleTranslate,SearchingBy=Keyword
#     )


# @when(u'Juan try to translate from english to spanish: {text}')
# def step_impl(context,text):
#     Juan.attemptsTo(
#         translate,The=text
#     )


# @then(u'Juan should see {Translation}')
# def step_impl(context,Translation):
#     Juan.shouldSee(
#         AsTranslation,The=Translation
#     )
    


    