var Ziggy = {
  baseUrl: "/",
  baseProtocol: "",
  baseDomain: "",
  basePort: null,
  defaultParameters: [],
  namedRoutes: {
    dashboard: { uri: "/", methods: ["GET"], middleware: ["auth"] },
    login: { uri: "/login", methods: ["GET"] },
    "login.attempt": { uri: "/login", methods: ["POST"] },
    logout: { uri: "/logout", methods: ["POST"] },
    "users.edit": {
      uri: "/users/{user}/edit",
      methods: ["GET"],
      middleware: ["auth"],
    },
    "users.create": {
      uri: "/users/create",
      methods: ["GET"],
      middleware: ["auth"],
    },
    "users.store": { uri: "/users", methods: ["POST"], middleware: ["auth"] },
    "users.update": {
      uri: "/users/{user}",
      methods: ["POST"],
      middleware: ["auth"],
    },
    users: { uri: "/users", methods: ["GET"], middleware: ["auth"] },
    "users.destroy": {
      uri: "/users/{user}",
      methods: ["DELETE"],
      middleware: ["auth"],
    },
  },
};

export { Ziggy };
