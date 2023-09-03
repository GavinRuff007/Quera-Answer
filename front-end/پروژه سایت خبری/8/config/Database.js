import { Sequelize } from "sequelize";

const db = new Sequelize("news_toplearn","news", "IvXg71s6!h(5DWu)", {
     host:"localhost",
     dialect: "mysql",
});



export default db;