package cz.jaan.karla.resources.accounts.DTO;

import cz.jaan.karla.resources.GenericDTO;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.List;

public class AccountDTO extends GenericDTO {

    private Integer id;
    private String name;

    public AccountDTO() {}

    public AccountDTO(byte[] byteArr) {

    }

    public byte[] toByteArray() throws IOException {
        List<Byte> byteList = new ArrayList<>(4 + 1 + name.length() + 1);
        addIntToList(byteList, id, 4);
        addStringToList(byteList, name);

        return super.toByteArray(byteList);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}
