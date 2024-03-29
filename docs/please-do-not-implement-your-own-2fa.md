---
hide:
  - navigation
---

# Please don't implement your own 2FA

Many big and seemingly well-respected companies, and even government, are implementing their own 2FA. 

TOTP exists and it is good. Just use it. Also don't use SMS or allow for fallback to SMS.

## Why you shouldn't implement your own 2FA

- It's annoying for users: no I do not want an app on my phone for each and every online account. Websites are fine
- It's insecure: TOTP apps have a well-tested pattern. If you deviate it, it will likely be less secure (see examples below)
- It's "too secure": people tend to think of security as 'stop someone breaking into my account'. In reality, a security threat model often includes 'availability' as well, so if your situation is 'I can't access my account because I dropped my phone in an ocean accidentally' then your account was probably less 'secure' than using "Passw0rd" as your password with no 2fa.

IF YOUR 2FA HAS THE OPTION TO FALL BACK TO SMS THEN IT IS NOT MORE SECURE THAN SMS.

## Examples

**The Dutch government.** Yes an entire government spent millions developing [Digid](https://en.wikipedia.org/wiki/DigiD). Not only is the UX far worse than a TOTP app (you have to go through a multistep process for each login, including entering a randomly generated key from the app to the website and then scanning a QR code generated by the website on the app), but it's also completely insecure. If you lose your phone, you just install the app again and get an SMS confirmation code, but they disabled the option to always authenticate with SMS because security.

**IBKR.** One of the biggest stockbroker platforms in the world. They also make you use "IB Key" to authenticate your logins, but if you lose your phone, you can use an SMS code to 'migrate' your key to a new phone.

## Why is TOTP good? 

TOTP lets me deal with all my 2FA accounts in one place. It has well-tested flows around losing access to your second factor (by generating 10 backup codes for each account). If you use open source apps like [Aegis](https://getaegis.app/), then you can also easily backup your codes, use them in multiple places, or migrate them to a new installation of the app.

Yes I know your users can't be trusted to manage their own security and you have to enforce best practices for them and stop them using '1234' as a password, but if you're going to take away control on the grounds of incompetence, then please be competent.


