var pathConfig={};
pathConfig.array = [
{
label:"homePage",
referenceUrl:"https://weather.com/",
url:"https://stage.weather.com/",
selectors:["a","b","c"]},
{
label:"todayPage",
referenceUrl:"https://weather.com/weather/today/l/USDC0001:1:US",
url:"https://stage.weather.com/weather/today/l/USDC0001:1:US",
selectors:""},
{
label:"houlryPage",
referenceUrl:"https://weather.com/weather/hourbyhour/l/USDC0001:1:US",
url:"https://stage.weather.com/weather/hourbyhour/l/USDC0001:1:US",
selectors:""},
{
label:"5day",
referenceUrl:"https://weather.com/weather/5day/l/USDC0001:1:US",
url:"https://stage.weather.com/weather/5day/l/USDC0001:1:US",
selectors:""},
{
label:"10day",
referenceUrl:"https://weather.com/weather/tenday/l/USDC0001:1:US",
url:"https://stage.weather.com/weather/tenday/l/USDC0001:1:US",
selectors:""}]
module.exports=pathConfig;
