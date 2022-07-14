class Solution {
    static int get_len(int carry){
        int len = 0;
        while(carry>0){
            len++;
            carry = (int)(carry/10);
        }
        return len;
    }
    
    public int[] plusOne(int[] digits) {
        int carry = 1, temp, remain;
        for(int i=digits.length-1; i>=0; i--){
            if(carry==0)
                break;
            temp = digits[i]+carry;
            carry = (int)(temp/10);
            digits[i] = temp%10;
        }
        if(carry>0){
            int[] result = new int[digits.length+1];
            result[0] = 1;
            for(int i=0; i<digits.length; i++)
                result[i+1] = digits[i];
            return result;
        }
        // if(carry>0){
        //     int lenOfCarry = get_len(carry);
        //     int[] result = new int[lenOfCarry+digits.length];
        //     for(int i=lenOfCarry+digits.length-1; i>=0; i--){
        //         if(i-lenOfCarry>=0)
        //             result[i] = digits[i-lenOfCarry];
        //         else{
        //             remain = carry%10;
        //             carry = (int)(carry/10);
        //             result[i] = remain;
        //         }
        //     }
        //     return result;
        // }
        return digits;
    }
}