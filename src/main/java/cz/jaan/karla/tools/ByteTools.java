package cz.jaan.karla.tools;

import java.nio.ByteBuffer;
import java.util.List;

public class ByteTools {

    /**
     * Convert List of Bytes to primitive byte array
     */
    public static byte[] toByteArray(List<Byte> byteList) {
        byte[] byteArr = new byte[byteList.size()];
        for (int i = 0; i < byteList.size(); i++)
            byteArr[i] = byteList.get(i);
        return byteArr;
    }

    /**
     * Concat primitive byte array to List of Bytes
     */
    public static void addByteArrToList(List<Byte> byteList, byte[] byteArray) {
        for (byte b : byteArray) byteList.add(b);
    }

    /**
     * Convert value into byteCount bytes (not less than 4)
     * and concat it to List of Bytes
     */
    public static void addIntToList(List<Byte> byteList, Integer value, int byteCount) {
        byte[] valueArr = ByteBuffer.allocate(byteCount).putInt(value).array();
        for (int i = 0; i < byteCount; i++)
            byteList.add(valueArr[i]);
    }

    /**
     * Convert value into 2 bytes and concat it to List of Bytes
     */
    public static void addShortToList(List<Byte> byteList, Integer value) {
        byte[] valueArr = ByteBuffer.allocate(2).putShort(value.shortValue()).array();
        for (int i = 0; i < 2; i++)
            byteList.add(valueArr[i]);
    }

    /**
     * Concat String value to List of Bytes with size of string as 2 byte value
     * at start of byte seq and add zero at the end (size is with the zero)
     */
    public static void addStringToList(List<Byte> byteList, String value) {
        int length = value.length();
        addShortToList(byteList, length + 1);
        for (int i = 0; i < length; i++)
            byteList.add((byte) value.charAt(i));
        byteList.add((byte) 0);
    }
}
