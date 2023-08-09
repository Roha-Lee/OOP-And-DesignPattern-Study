import { Subject, Observer } from './interface';

export class WeatherData implements Subject {
    observers: Array<Observer>;
    temperature: number;
    humidity: number;
    pressure: number;

    constructor() {
        this.temperature = 0;
        this.humidity = 0;
        this.pressure = 0;
        this.observers = [];
    }
    registerObserver(o: Observer): void {
        this.observers.push(o);
    }

    removeObserver(o: Observer): void {
        const index = this.observers.indexOf(o);
        if (index > -1) {
            this.observers.splice(index, 1);
        }
    }
    notifyObservers(): void {
        this.observers.forEach((observer) => {
            observer.update();
        });
    }
    getTemperature() {
        return this.temperature;
    }
    getHumidity() {
        return this.humidity;
    }
    getPressure() {
        return this.pressure;
    }
    setMeasurement(temperature: number, humidity: number, pressure: number) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        this.measurementsChanged();
    }
    measurementsChanged() {
        this.notifyObservers();
    }
}