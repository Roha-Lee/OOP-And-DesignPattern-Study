import { CurrentConditionsDisplay } from './current-conditions-display';
import { StatisticsDisplay } from './statistics-display';
import { ForecastDisplay } from './forecast-display';

export class WeatherData {
    currentConditionsDisplay: CurrentConditionsDisplay;
    statisticsDisplay: StatisticsDisplay;
    forecastDisplay: ForecastDisplay;
    constructor() {
        this.currentConditionsDisplay = new CurrentConditionsDisplay();
        this.statisticsDisplay = new StatisticsDisplay();
        this.forecastDisplay = new ForecastDisplay();
    }
    precisionWithN(n: number, value: number) {
        return Math.floor(Math.pow(10, n) * value) / Math.pow(10, n);
    }
    getTemperature() {
        return this.precisionWithN(2, Math.random() * 10 + 20);
    }
    getHumidity() {
        return this.precisionWithN(2, Math.random() * 30 + 50);
    }
    getPressure() {
        return this.precisionWithN(2, Math.random() * 10 + 1000);
    }
    measurementsChanged() {
        const temperature = this.getTemperature();
        const humidity = this.getHumidity();
        const pressure = this.getPressure();

        // display
        this.currentConditionsDisplay.update(temperature, humidity, pressure);
        this.statisticsDisplay.update(temperature, humidity, pressure);
        this.forecastDisplay.update(temperature, humidity, pressure);
    }
}