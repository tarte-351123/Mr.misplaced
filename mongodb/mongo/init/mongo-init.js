var users = [
  {
    user: "root",
    pwd: "password",
    roles: [
      {
        role: "dbOwner",
        db: "staywatch"
      }
    ]
  }
];

for (var i = 0, length = users.length; i < length; ++i) {
  db.createUser(users[i]);
}