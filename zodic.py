import sys
import subprocess
def installPyaztro():
    subprocess.check_call([sys.executable, '-m','pip', 'install', 'pyaztro'])

def zoidc():
    try:
        sign = input("Zodic Sign: ").lower()
        zodicSign = pyaztro.Aztro(sign = sign)
        print(f"Sign: {zodicSign.sign.capitalize()}\n")
        print(f"Desctiption:\n {zodicSign.description}\n")
        print(f"You will be {zodicSign.mood.capitalize()} today.")
        print(f"Your Lucky Color is {zodicSign.color}.")
        print(f"Your Lucky Partner is {zodicSign.compatibility}.")
        print(f"Your Lucky Time is {zodicSign.lucky_time}.")
        print(f"Your Lucky Number is {zodicSign.lucky_number}.\n")
    except:
        print("No Found!")
        zoidc()

if __name__ == "__main__":
    try:
        import pyaztro
    except:
        installPyaztro()
        import pyaztro
    finally:
        zoidc()

signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
