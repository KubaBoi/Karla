package cz.jaan.karla.resources.accounts;

import cz.jaan.karla.resources.GenericEntity;
import jakarta.persistence.*;

@Entity
public class Account extends GenericEntity {

    @Id
    @GeneratedValue(strategy=GenerationType.SEQUENCE, generator="account_seq")
    @SequenceGenerator(name="account_seq", sequenceName = "account_seq", allocationSize = 1)
    private Integer id;
    private String name;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
