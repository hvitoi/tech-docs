class Main {
	public static void main(String[] args) {

		boolean isAlien = true; // Good convention to use "is" with boolean variables
		if (isAlien == true) {
			System.out.println("It is an alien.");
		} else if (isAlien == false) {
			System.out.println("It's not an alien.");
		} else {
			System.out.println("It will never reach here");
		}

		int topScore = 80;
		if (topScore < 100) {
			System.out.println("You got the high score!");
		}

		// AND
		int secondTopScore = 95;
		if ((topScore > secondTopScore) && (topScore < 100)) {
			System.out.println("Greater than second top score and less than 100");
		}

		// OR
		if ((topScore > 90) || (secondTopScore <= 90)) {
			System.out.println("Either or both of the conditions are true");
		}

		// NOT
		boolean isCar = false;
		if (!isCar) {
			System.out.println("This is not supposed to happen");
		}

		// Ternary operator
		isCar = true;
		boolean wasCar = isCar ? true : false;
		if (wasCar) {
			System.out.println("wasCar is true");
		}

		double myFirstValue = 20.00d;
		double mySecondValue = 80.00d;
		double myValuesTotal = (myFirstValue + mySecondValue) * 100.00d;
		System.out.println("MyValuesTotal = " + myValuesTotal);

		double theRemainder = myValuesTotal % 40.00d;
		System.out.println("theRemainder = " + theRemainder);

		boolean isNoRemainder = (theRemainder == 0) ? true : false;
		System.out.println("isNoRemainder = " + isNoRemainder);
		if (!isNoRemainder) {
			System.out.println("Got some remainder");
		}
	}
}
