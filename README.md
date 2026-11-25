# StudyHive
An app where students can share notes, files and study resources with each other.


Description: 
Study material kinda gets lost in group chats and random cloud folders. StudyHive will give it all a home. Users can
follow classmates, join course groups and share notes, PDF's and links in a feed where others can comment, like 
and save them. 

Agile planning:

We agreed to use Scrum with 2 week sprints and keeping track of tasks via discord and github project board. 

Sprints will look like this with goals and dates attached >>> .... (exact dates are subject to change)
----------------------------------------------------------------------------
Sprints:

Sprint 0 (Oct 19 – Oct 23): Project idea, README, GitHub repo and Django setup

Sprint 1 (Oct 26 – Nov 6): Sign up, login, profiles and posting (stories 1–3)

Sprint 2 (Nov 9 – Nov 20): Following, groups, post visibility and the feed (stories 4–7)

Sprint 3 (Nov 23 – Dec 4): Comments, likes and search (stories 8–9)

Sprint 4 (Dec 7 – Dec 11): Testing, bug fixes and final presentation


----------------------------------------------------------------------------
## What works now

- **Sign up** – create an account with a username and password
- **Log in** – with an error message for a wrong username or password
- **Log out** – returns you to the home page

| Page | Address |
|---|---|
| Home | `/` |
| Sign up | `/accounts/signup/` |
| Log in | `/accounts/login/` |
| Log out | `/accounts/logout/` (logs out, then goes back to `/`) |
| Admin | `/admin/` |

## Run it locally

You need Python 3.12 or newer.

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000 and click **Sign up**.
To use the admin panel, first make an admin account with `python manage.py createsuperuser`.

## Project layout

```
manage.py
requirements.txt
testproject/        settings.py and urls.py (project setup)
testApp/            views.py (sign-up page)
templates/
  base.html         nav bar and shared styles
  home.html         home page
  registration/
    login.html      log in page
    signup.html     sign up page
StudyHive-prototype/  prototype slides and screenshots
```

## Prototype: Log in & Log out (Sprint 1)

Screens from the working Django app. Full slides: [StudyHive-Login-Prototype.pptx](StudyHive-prototype/docs/prototype/StudyHive-Login-Prototype.pptx) (click it, then **Download raw file**).

**How it works:** Home page → Log in → Django checks the username and password → Welcome page → Log out → back to the home page. A wrong password keeps you on the login page with an error.

| 1. Home page (logged out) | 2. Login page |
|---|---|
| ![Home page while logged out](StudyHive-prototype/docs/prototype/1_home_logged_out.png) | ![Login page](StudyHive-prototype/docs/prototype/2_login_page.png) |
| **3. Wrong password** | **4. Logged in** |
| ![Login page showing a wrong password error](StudyHive-prototype/docs/prototype/3_wrong_password.png) | ![Home page greeting the logged-in user](StudyHive-prototype/docs/prototype/4_home_logged_in.png) |

## User Stories:
https://docs.google.com/document/d/1_PYDvJ2irWRj8_Yq2fsUAcu7ec4PU6Rp57_7O86sbQk/edit?tab=t.0
