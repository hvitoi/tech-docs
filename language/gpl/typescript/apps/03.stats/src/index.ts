// Classes
import { CsvFileReader } from './CsvFileReader';
import { FootballReader } from './FootballReader';
import { Summary } from './Summary';
import { WinsAnalysis } from './analyzers/WinsAnalysis';
import { ConsoleReport } from './reportTargets/ConsoleReport';
import { HtmlReport } from './reportTargets/HtmlReport';

// ---
// READ AND PARSE

// COMPOSITION APPROACH
const reader = new CsvFileReader('football.csv'); // Read the csv
const football = new FootballReader(reader); // Feed the data into FootballReader
football.load(); // Parse the data

// With static methods
const reader2 = FootballReader.fromCsv('football.csv');

// ---
// ANALYZE AND OUTPUT

// COMPOSITION APPROACH
const winsAnalysis = new WinsAnalysis('Man United');
const consoleReport = new ConsoleReport();
const summary = new Summary(winsAnalysis, consoleReport);
summary.buildAndPrintReport(football.matches);

// html report
const htmlReport = new HtmlReport();
const summary2 = new Summary(winsAnalysis, htmlReport);
summary2.buildAndPrintReport(football.matches);

// html report calling a static method
Summary.winsAnalysisWithHtmlReport('Man United');
