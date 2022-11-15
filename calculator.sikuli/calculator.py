
# ===== open app =====
PathApp = "C:\Windows\System32\calc.exe"
App.open(PathApp)

# ===== action =====
click("1668505117617.png")
click("1668505635203.png")
click("1668505215231.png")
click("1668505232299.png")
click("1668505237143.png")

# ===== assert =====
type('c', KEY_CTRL)
result = Env.getClipboard()
print 'result = ' + result

assert result == '25'




