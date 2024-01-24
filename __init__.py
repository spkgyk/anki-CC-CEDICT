from aqt import mw, gui_hooks
from aqt.editor import EditorWebView
from aqt.qt import QAction, QKeySequence, QShortcut

from .forms import dict_ui
from .cedict.main import start_main


def open_dict():
    mw.dict = start_main(dict_ui.Ui_Dialog())
    mw.dict.pop_out_dict()


def s_hotkey_press(webview: EditorWebView):
    if not hasattr(mw, "dict"):
        mw.dict = start_main(dict_ui.Ui_Dialog())
    selected_text = webview.selectedText()
    if selected_text and type(selected_text) == str:
        mw.dict.pop_out_dict()
        mw.dict.search_text(selected_text)


def init_ctrl_s_hotkey(webview: EditorWebView):
    shortcut_ctrl_s = QShortcut(QKeySequence("Ctrl+S"), webview)
    shortcut_ctrl_s.activated.connect(lambda webview=webview: s_hotkey_press(webview))


action = QAction("CC-CEDICT for Anki", mw)
action.triggered.connect(open_dict)
mw.form.menuTools.addAction(action)
action.setShortcut(QKeySequence("Ctrl+D"))


gui_hooks.editor_web_view_did_init.append(init_ctrl_s_hotkey)
