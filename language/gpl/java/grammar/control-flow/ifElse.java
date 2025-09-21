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

		// AND
		int foo = 80;
		if ((foo > 0) && (foo < 100)) {
			System.out.println("It's between 0 and 100.");
		}

		// OR
		if ((foo < 0) || (foo > 100)) {
			System.out.println("It's negative or greater than 100");
		}

		// NOT
		boolean isCar = false;
		if (!isCar) {
			System.out.println("This is not supposed to happen");
		}
	}
}
