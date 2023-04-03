public class HuffmanEncoder {
    private String text;
    public Message msgObject;
    private HuffmanTree huffmanTree;

    // LinkedList named charset to store each distinct character along
    // with its new sequence and frequency, after traversing the tree
    private CharLinkedList charset;
    private boolean hasBeenCompressed;

    public HuffmanEncoder(String text) {
        this(new Message(text));
    }

    public HuffmanEncoder(Message msg) {
        this.msgObject = msg;
        this.text = msgObject.getMessage();
        huffmanTree = new HuffmanTree(msgObject);
        charset = new CharLinkedList();
        hasBeenCompressed = false;
    }

    public void compress() {
        lookUp(huffmanTree.getRoot(), "");
        hasBeenCompressed = true;
    }
    // Traversing the tree edges and building a new sequence for each
    // distinct character.
    public void lookUp(Node node, String s) {
        if(!node.isLeaf()) {
            lookUp(node.left, s + "0");
            lookUp(node.right, s + "1");
        } else {
            // When we hit a leaf node, we add its character, new sequence, and its frequency
            // to the linked list 'charset'
            charset.add(node.character, s, node.frequency);
        }
    }

    // This method returns the new size of the message after traversing
    // the huffman tree
    public int getSizeOfSequence() {
        if(!hasBeenCompressed)
            throw new RuntimeException("ERROR: Message has not been compressed!");
        int totalSize = 0;
        int bits = 0;
        CharNode n = charset.getLink();
        while(n != null) {
            totalSize += n.frequency * n.bit_size.length();
            bits += n.bit_size.length();
            n = n.next;
        }
        totalSize += (Message.CHAR_SIZE * charset.size()) + bits;
        return totalSize;
    }

    // returns the percentage of decrease in the size of the message
    // after compression
    public double howMuchCompressed() {
        if(!hasBeenCompressed)
            throw new RuntimeException("ERROR: Message has not been compressed!");
        return ((msgObject.getSize() - getSizeOfSequence()) /
                (double) msgObject.getSize()) * 100 ;
    }

    public CharLinkedList get_charset() {
        return charset;
    }

    // Returns the compressed binary representation of the WHOLE message
    public String[] compressedBinaryCode() {
        if(!hasBeenCompressed)
            throw new RuntimeException("ERROR: Message has not been compressed!");
        String[] d = new String[text.length()];
        for(int i = 0; i < text.length(); i++) {
            d[i] = charset.getCharNode(text.charAt(i)).bit_size;
        }
        return d;
    }

    public void indivSequence() {
        if(!hasBeenCompressed)
            throw new RuntimeException("ERROR: Message has not been compressed!");
        CharNode trav = charset.getLink();
        while(trav != null) {
            System.out.println(trav.ch + ": " + trav.bit_size);
            trav = trav.next;
        }
    }

    public static void main(String[] args) {
        HuffmanEncoder hencoder = new HuffmanEncoder("Siam unfurling the same snow-white quadruped in the royal standard; and the Hanoverian flag bearing the one figure of a snow-white charger; and the great Austrian Empire, Caesarian, heir to overlording Rome, having for the imperial colour the same imperial hue; and though this pre-eminence in it applies to the human race itself, giving the white man ideal mastership over every dusky tribe; and though, besides, all this, whiteness has been even made significant of gladness, for among the Romans a white stone marked"
        );
        hencoder.compress();
        System.out.println(hencoder.msgObject.getSize());
        System.out.println(hencoder.getSizeOfSequence());
    }
}
