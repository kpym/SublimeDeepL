import sublime
import sublime_plugin
import webbrowser
import urllib.parse





def tourl(str):
    str = str.replace('/', r'\/').replace('|', r'\|')
    return urllib.parse.quote(str, safe='')

class DeeplTranslateCommand(sublime_plugin.TextCommand):
    """
    This will open wwww.deepl.com to translate a word or a selection.
    """
    def run(self, edit):
        region = self.view.sel()[0];
        if not region.empty():
            phrase = self.view.substr(region)
        else:
            phrase = self.view.substr(self.view.word(region.begin()))
        sublime.status_message('open DeepL Translate...')
        webbrowser.open_new_tab('https://www.deepl.com/translator#en/en/' + tourl(phrase))

class DeeplRewriteCommand(sublime_plugin.TextCommand):
    """
    This will open wwww.deepl.com to translate a word or a selection.
    """
    def run(self, edit):
        region = self.view.sel()[0];
        if not region.empty():
            phrase = self.view.substr(region)
        else:
            phrase = self.view.substr(self.view.word(region.begin()))
        sublime.status_message('open DeepL Rewrite...')
        webbrowser.open_new_tab('https://www.deepl.com/write/#en/' + tourl(phrase))
