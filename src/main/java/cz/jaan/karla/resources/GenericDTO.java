package cz.jaan.karla.resources;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.List;

public class GenericDTO {

    protected byte[] toByteArray(List<Byte> byteList) throws IOException {
        byte[] byteArr = new byte[byteList.size()];
        for (int i = 0; i < byteList.size(); i++)
            byteArr[i] = byteList.get(i);
        return byteArr;
    }

    protected void addIntToList(List<Byte> byteList, Integer value, int byteCount) {
        byte[] valueArr = ByteBuffer.allocate(byteCount).putInt(value).array();
        for (int i = 0; i < byteCount; i++)
            byteList.add(valueArr[i]);
    }

    protected void addStringToList(List<Byte> byteList, String value) {
        int length = value.length();
        byteList.add((byte) (length + 1));
        for (int i = 0; i < length; i++)
            byteList.add((byte) value.charAt(i));
        byteList.add((byte) 0);
    }
}
