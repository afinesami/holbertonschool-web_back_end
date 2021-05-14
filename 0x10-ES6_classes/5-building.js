export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building
      && this.evacuationWarningMessage === undefined) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
