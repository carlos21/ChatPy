db = db.getSiblingDB('admin')

db.createUser({
    user: 'administrator',
    pwd: 'no1willguess',
    roles: [{
        role: 'userAdminAnyDatabase', db: 'admin'
    }]
});

db = db.getSiblingDB('chatpy')

db.createUser({
    user: 'chatpy-user',
    pwd: 'secret',
    roles: [{
        role: 'readWrite',
        db: 'chatpy'
    }]
});

db.auth('chatpy-user', 'secret')

db.user.save({email: 'darkzeratul64@gmail.com', first_name: 'Carlos', last_name: 'Duclos', password: '9954ec587edcc4645634024fdc15ed408d7c7240e3c78a4b7200b9744b7fe18a'})