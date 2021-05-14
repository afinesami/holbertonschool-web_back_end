import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    const clone = new (
      Object.getPrototypeOf(this.constructor))(this._brand, this._motor, this._color);
    clone._range = this._range;
    return clone;
  }
}
