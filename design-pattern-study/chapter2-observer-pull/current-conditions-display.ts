import { Observer, DisplayElement } from './interface';
import { WeatherData } from './weather-data';
export class CurrentConditionsDisplay implements Observer, DisplayElement{
    temperature: number;
    humidity: number;
    pressure: number;
    weatherData: WeatherData;
    constructor(weatherData: WeatherData) {
        this.temperature = 0;
        this.humidity = 0;
        this.pressure = 0;
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }
    update() {
        this.temperature = this.weatherData.getTemperature();
        this.humidity = this.weatherData.getHumidity();
        this.pressure = this.weatherData.getPressure();
        this.display();
    }
    display() {
        console.log(`현재 상태: 온도 ${this.temperature}도, 습도 ${this.humidity}%, 기압 ${this.pressure}`);
    }
}