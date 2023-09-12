package cz.jaan.karla.resources.accounts.DTO;

import cz.jaan.karla.resources.GenericDTO;
import cz.jaan.karla.resources.accounts.Account;
import cz.jaan.karla.tools.ByteTools;

import java.util.ArrayList;
import java.util.List;

public class AccountDTO extends GenericDTO {

    private Integer id;
    private String name;

    public AccountDTO() {
    }

    public AccountDTO(Account account) {
        this.id = account.getId();
        this.name = account.getName();
    }

    @Override
    public byte[] toByteArray() {
        List<Byte> byteList = new ArrayList<>(4 + 2 + name.length() + 1);
        ByteTools.addIntToList(byteList, id, 4);
        ByteTools.addStringToList(byteList, name);

        return ByteTools.toByteArray(byteList);
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
