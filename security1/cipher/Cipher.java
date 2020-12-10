package cipher;

import org.w3c.dom.ls.LSOutput;

import java.util.stream.Collectors;

interface CipherAlgorithm {
    public String encrypt(String msg);
    public String decrypt(String msg);
}


class AffineCipher implements CipherAlgorithm {

    int a, b;

    public AffineCipher(int a, int b) {
        this.a = a;
        this.b = b;
    }

    @Override
    public String encrypt(String msg) {
        StringBuilder sb = new StringBuilder();

        for(char ch: msg.toCharArray()) {
            if(Character.isUpperCase(ch)) {
                sb.append((char)((a * (ch - 'A') + b) % 26 + 'A'));
            } else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }

    @Override
    public String decrypt(String msg) {
        int a_inv = -1;
        for (int i = 0; i < 26; ++i) {
            if (a * i % 26 == 1) a_inv = i;
        }

        StringBuilder sb = new StringBuilder();

        for (char ch : msg.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                sb.append((char) ((a_inv * (ch - b + 'A') % 26) + 'A'));
            } else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}

class CaesarCipher implements CipherAlgorithm {

    int shift;

    public CaesarCipher(int shift) {
        this.shift = shift % 26;
    }

    @Override
    public String encrypt(String msg) {
        StringBuilder sb = new StringBuilder();

        for(char ch: msg.toCharArray()) {
            if(Character.isUpperCase(ch)) {
                sb.append((char)((ch - 'A' + shift) % 26 + 'A'));
            } else {
                sb.append(ch);
            }
        }

        return sb.toString();
    }

    @Override
    public String decrypt(String msg) {
        return new CaesarCipher(26 - shift).encrypt(msg);
    }
}

public class Cipher {
    public static void main(String[] args) {
        CipherAlgorithm c = new AffineCipher(19 , 23);
        String message = "HELLO WORLD";
        String encryptedMessage = c.encrypt(message);
        String decryptedMessage = c.decrypt(encryptedMessage);

        System.out.println("Message = " + message);
        System.out.println("Encrypted = " + encryptedMessage);
        System.out.println("Decrypted = " + decryptedMessage);
    }
}
