package cz.jaan.karla;

import cz.jaan.karla.resources.accounts.DTO.AccountDTO;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@RestController
public class HelloController {

    @GetMapping("/")
    public byte[] index(@RequestBody byte[] inputBytes) throws IOException {
        AccountDTO accountDTO = new AccountDTO();
        accountDTO.setId(0);
        accountDTO.setName("Ahoj");
        return accountDTO.toByteArray();
    }

}
