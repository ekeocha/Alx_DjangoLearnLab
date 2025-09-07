Perfect 👍

Here’s **Step 6: Documentation** for your authentication system:

---

# 📖 Authentication System Documentation

## 1. **Overview**

This authentication system handles user **registration, login, logout, and profile management** using Django’s built-in authentication views and custom extensions.

* **Registration** → Uses an extended `UserCreationForm` to collect username, email, password, and additional fields.
* **Login/Logout** → Uses Django’s built-in views (`LoginView`, `LogoutView`).
* **Profile Management** → Custom view that allows authenticated users to update profile details (email, profile picture, bio, etc.).
* **Security** → CSRF tokens enabled, passwords hashed with Django’s default PBKDF2 algorithm.

---

## 2. **Authentication Flow**

1. **Registration (/register)**

   * User fills in registration form.
   * After successful submission, user account is created and redirected to login.

2. **Login (/login)**

   * User provides valid credentials.
   * If authenticated, Django creates a session and logs in the user.

3. **Logout (/logout)**

   * User session is terminated.
   * User is redirected to home or login page.

4. **Profile (/profile)**

   * Authenticated users can view and update details.
   * Changes are saved to the `Profile` model and linked to the `User`.

---

## 3. **How to Test Each Feature**

### 🔹 Registration

* Go to `/register`.
* Enter **username, email, password, confirm password**.
* Submit → Verify that the new user is saved in the database (`User` + `Profile`).

### 🔹 Login

* Go to `/login`.
* Enter valid credentials.
* Verify successful login (you should see profile or dashboard).
* Enter invalid credentials → Ensure error message is shown.

### 🔹 Logout

* After login, click "Logout".
* Verify that you are redirected and session is cleared.

### 🔹 Profile Management

* Go to `/profile`.
* Update profile details (email, bio, profile picture).
* Submit → Ensure changes are reflected in DB.

---

## 4. **Security Considerations**

* ✅ **CSRF Protection** → All forms include `{% csrf_token %}`.
* ✅ **Password Hashing** → Django stores passwords securely using PBKDF2.
* ✅ **Access Control** → Profile page is only accessible to authenticated users (`@login_required`).
* ✅ **Validation** → User input is validated with Django forms.
* ✅ **Sessions** → Django manages secure sessions.

---

## 5. **Setup Notes**

* Install Pillow for image uploads:

  ```bash
  pip install Pillow
  ```
* Ensure `static` directory exists or update `STATICFILES_DIRS` in `settings.py`.

---

✅ With this, your authentication system is **complete, secure, and documented**.

## Blog Post CRUD

- List posts: GET /posts/
- View post:  GET /posts/<pk>/
- Create post: (auth) GET/POST /posts/new/
- Edit post:   (author only) GET/POST /posts/<pk>/edit/
- Delete post: (author only) POST /posts/<pk>/delete/

Permissions:
- Anyone can view list & detail.
- Only authenticated users can create.
- Only the author can edit or delete their own posts.



