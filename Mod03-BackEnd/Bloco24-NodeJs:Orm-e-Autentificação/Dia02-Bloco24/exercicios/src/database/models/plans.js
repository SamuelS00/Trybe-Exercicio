module.exports = (sequelize, DataTypes) => {
  const Plan = sequelize.define('Plans', {
    plan_id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
    coverage: DataTypes.STRING,
    price: DataTypes.DOUBLE,
  },
  {
    timestamps: false,
    tableName: 'Plans',
    underscored: true,
  });

  Plan.associate = (models) => {
    Plan.belongsTo(models.Patients, { foreingKey: 'plan_id', as: 'patients'})
  };

  return Plan;
}