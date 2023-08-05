import { Observer, DisplayElement } from './interface';
import { WeatherData } from './weather-data';
class Statistics {
    maxValue: number;
    minValue: number;
    numReadings: number;
    constructor() {
        this.maxValue = 0;
        this.minValue = 200;
        this.numReadings = 0;
    }
    update(value: number) {
        this.numReadings++;
        this.maxValue = Math.max(this.maxValue, value);
        this.minValue = Math.min(this.minValue, value);
        this.display();
    }
    display() {
        console.log(`통계: 최대 ${this.maxValue}, 최소 ${this.minValue}, 누적갱신 ${this.numReadings}`);
    }
}

export class StatisticsDisplay implements Observer, DisplayElement{
    tempStatistics: Statistics;
    humidityStatistics: Statistics;
    pressureStatistics: Statistics;
    weatherData: WeatherData;
    constructor(weatherData: WeatherData) {
        this.tempStatistics = new Statistics();
        this.humidityStatistics = new Statistics();
        this.pressureStatistics = new Statistics();
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }
    update(temperature: number, humidity: number, pressure: number) {
        this.tempStatistics.update(temperature);
        this.humidityStatistics.update(humidity);
        this.pressureStatistics.update(pressure);
        this.display();
    }
    display() {
        this.tempStatistics.display();
        this.humidityStatistics.display();
        this.pressureStatistics.display();
    }
}