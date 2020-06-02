from clnch import *
# 時間計算
class commandline_TimeCalculator:

    def __init__( self, use_history=False ):
        self.use_history = use_history

    def onCandidate( self, update_info ):
        return []
    
    def onEnter( self, commandline, text, mod ):
        import re
   
        m = re.match("(\d+:\d+)([-+])(\d+:\d+)", text)
        if not m:
            return False
                
        try:
            import datetime
            
            t1 = datetime.datetime.strptime(m.group(1), "%H:%M")
            t2 = datetime.datetime.strptime(m.group(3), "%H:%M")
            # print(t1)
            # print(t2)
            if m.group(2) == '-':
                d  = t1 - t2
            else:
                d = t1 + t2
            result_string = str(d)
            commandline.setText(result_string )
            commandline.selectAll()
            print(f"{text}={result_string}")
            if self.use_history:
                commandline.appendHistory( text )
            setClipboardText(result_string)
            return True
        except Exception as e:
            print(e)
            return False

    def onStatusString( self, text ):
        return None

