// 75% runtime, 57% memory
// Yep...not that comfortable in C# atm
namespace PlusOne 
{
    public class Solution_v2 {
        public int[] PlusOne(int[] digits) {
            int length = digits.Length;
            for (int i = length - 1; i >= 0; i--)
            {
                // Clever - Only need to move to next digit if digit is 9
                if (digits[i] < 9) {
                    digits[i] += 1;
                    return digits;
                }
                digits[i] = 0;
            }
            int[] newNumber = new int[length + 1];
            // Clever again - the only time you reach here is if the entire number if zeroed out
            newNumber[0] = 1;
            return newNumber;
        }
    }

    public class Solution {
        public int[] PlusOne(int[] digits) {
            int length = digits.Length;
            int carry = 1;
            int i = length - 1;
            while (i >= 0) {
                int digit_sum = digits[i] + carry;
                digits[i] = digit_sum % 10;
                // Will C# round this down?
                carry = digit_sum / 10;
                if (carry == 0) {
                    return digits;
                }
                i -= 1;
            }

            if (carry == 1) {
                int[] new_digits = new int[length + 1];
                new_digits[0] = 1;
                i = 0;
                while (i < length) {
                    new_digits[i + 1] = digits[i];
                    i += 1;
                }
                return new_digits;
            } else {
                return digits;
            }
        }
    }
}
