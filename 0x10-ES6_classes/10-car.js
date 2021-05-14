export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const origin = this;
    return Object.assign(Object.create(Object.getPrototypeOf(origin)), {
      _brand: undefined,
      _motor: undefined,
      _color: undefined,
    });
  }
}
