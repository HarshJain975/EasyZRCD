import java.util.*;
public class Message {
    private final String text;
    static final int CHAR_SIZE = 8;
    private final int ALPHABET_SIZE = 256;
    private final char[] characters;
    private final int[] frequencyOfChars;

    Message(final String text) {
        if(text.length() <= 0)
            throw new RuntimeException("Error: Message size <= 0");
        this.text = text;
        characters = getChars();
        frequencyOfChars = buildFrequencyTable();
    }

    public String getMessage() { return text; } // returns message itself.
    public int getTotalFrequency() { return text.length(); } // returns length of the message
    public char[] getCharacters() { return characters; } // returns array of distinct characters
    // returns integer array containing frequency of each distinct character 'i' at a[i]
    public int[] getFrequencies() { return frequencyOfChars; }
    // returns true if message string is empty.
    public boolean isEmpty() { return getTotalFrequency() == 0; }

    // returns size of a binary sequence for the message
    public int getSize() {
        return CHAR_SIZE * getTotalFrequency();
    }

    // This method returns the array of distinct characters
    private char[] getChars() {
        List list = new ArrayList<Character>();
        list.add(text.charAt(0));
        for (int i = 0; i < getTotalFrequency(); i++) {
            if (!list.contains(text.charAt(i)))
                list.add(text.charAt(i));
        }
        char[] myChars = new char[list.size()];
        for (int i = 0; i < list.size(); i++)
            myChars[i] = (Character) list.get(i);
        return myChars;
    }

    // Calculates the number of times a given character appears in the string.
    public int calcFrequencyOfChar(final char ch) {
        int charFreq = 0;
        for(int i = 0; i < getTotalFrequency(); i++) {
            if(text.charAt(i) == ch)
                charFreq++;
        }
        return charFreq;
    }

    // Builds frequency table of each distinct character, returns an integer array
    // containing frequency of each distinct character 'i' at a[i].
    private int[] buildFrequencyTable() {
        int[] frequencies = new int[ALPHABET_SIZE];
        for(final char ch : text.toCharArray()) {
            frequencies[ch]++;
        }
        return frequencies;
    }

    // returns the binary representation of the message
    public String binaryCode() {
        String binarySequence = new String();
        for(int i = 0; i < getTotalFrequency(); i++) {
            binarySequence += convertBinary(getMessage().charAt(i));
        }
        return binarySequence;
    }

    // returns binary sequence of distinct characters
    public String[] binaryOfChars() {
        String[] binarySequence = new String[characters.length];
        for(int i = 0; i < characters.length; i++) {
            binarySequence[i] = convertBinary(characters[i]);
        }
        return binarySequence;
    }

    // Helper method to convert a given decimal number into a binary sequence
    // in the form of string.
    public String convertBinary(int decimal) {
        String binary="";
        while(decimal>0)
        {
            binary=(decimal%2)+binary;
            decimal=decimal/2;
        }

        String str =new String(), zeros ="0";
        if(binary.length()!= 8)
        {
            while(str.length() != 8)
            {
                str = zeros + binary;
                zeros += "0";
            }
        }

        return str;
    }
}
