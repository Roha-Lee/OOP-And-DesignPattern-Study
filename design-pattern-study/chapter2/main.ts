import { WeatherData } from './weather-data';

const weatherData = new WeatherData();
for (let i = 0; i < 10; i++) {
    weatherData.measurementsChanged();
}

