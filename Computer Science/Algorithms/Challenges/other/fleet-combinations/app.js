const chooseFleets = (wheels) => {
  const fleetCombinations = wheels.map((wheel) => {
    if (wheel % 2 !== 0) {
      return 0;
    } else {
      return Math.floor(wheel / 4) + 1;
    }
  });
  return fleetCombinations;
};

// const combinations = chooseFleets([4, 5, 6]);
// console.log(combinations);

module.exports = { chooseFleets };
