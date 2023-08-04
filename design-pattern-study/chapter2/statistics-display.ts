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

export class StatisticsDisplay {
    tempStatistics: Statistics;
    humidityStatistics: Statistics;
    pressureStatistics: Statistics;
    constructor() {
        this.tempStatistics = new Statistics();
        this.humidityStatistics = new Statistics();
        this.pressureStatistics = new Statistics();
    }
    update(temperature: number, humidity: number, pressure: number) {
        this.tempStatistics.update(temperature);
        this.humidityStatistics.update(humidity);
        this.pressureStatistics.update(pressure);
    }
    display() {
        this.tempStatistics.display();
        this.humidityStatistics.display();
        this.pressureStatistics.display();
        console.log();
    }
}