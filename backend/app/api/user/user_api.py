@app.post("/register")
async def register(user: UserCreate):
    return create_user(user)

# Войти в систему
@app.post("/login")
async def login(user: UserLogin):
    return authenticate_user(user)

# Выйти из системы (это просто пример, без реальной аутентификации с токеном)
@app.post("/logout/")
async def logout():
    return {"message": "Logged out successfully"}
