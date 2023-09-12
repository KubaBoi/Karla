package cz.jaan.karla.resources;

import cz.jaan.karla.tools.ByteTools;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class GenericDTO {

    /**
     * Convert List of DTOs to primitive byte array<br>
     * with 2 byte size value at start od byte seq
     */
    public static byte[] listDTOsToBytes(List<? extends GenericDTO> DTOs) throws IOException {
        List<Byte> byteList = new ArrayList<>();
        ByteTools.addShortToList(byteList, DTOs.size());
        for (GenericDTO DTO : DTOs)
            ByteTools.addByteArrToList(byteList, DTO.toByteArray());

        return ByteTools.toByteArray(byteList);
    }

    public byte[] toByteArray() {
        return null;
    }

    /*public static List<? extends GenericDTO> toDTOList(
            Iterable<? extends GenericEntity> entites,
            Class<? extends GenericDTO> DTOClass) throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
        List<? extends GenericDTO> DTOs = new ArrayList<>();
        for (GenericEntity entity : entites)
            DTOs.add(DTOClass.getDeclaredConstructor(GenericEntity.class).newInstance(entity));
        return DTOs;
    }*/
}
