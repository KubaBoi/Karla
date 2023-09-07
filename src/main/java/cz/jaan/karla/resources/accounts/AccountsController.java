package cz.jaan.karla.resources.accounts;

import cz.jaan.karla.resources.accounts.DTO.AccountDTO;
import cz.jaan.karla.resources.accounts.DTO.CreateAccountDTO;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RestController
public class AccountsController {

    @GetMapping("/accounts")
    public ResponseEntity<AccountDTO> accounts() {

        AccountDTO accountDTO = new AccountDTO();
        accountDTO.setId(0);
        accountDTO.setName("Ahoj");

        return new ResponseEntity<>(accountDTO, HttpStatus.I_AM_A_TEAPOT);
    }

    @GetMapping("/bin/accounts")
    public ResponseEntity<byte[]> accountsBin() throws IOException {

        AccountDTO accountDTO = new AccountDTO();
        accountDTO.setId(15);
        accountDTO.setName("Ahoj");

        return new ResponseEntity<>(accountDTO.toByteArray(), HttpStatus.I_AM_A_TEAPOT);
    }

    @PostMapping("/accounts/create")
    public ResponseEntity<AccountDTO> createAccount(@RequestBody CreateAccountDTO newAccount) {
        AccountDTO accountDTO = new AccountDTO();
        accountDTO.setId(0);
        accountDTO.setName(newAccount.getName());
        return new ResponseEntity<>(accountDTO, HttpStatus.OK);
    }

    @GetMapping("/accounts/{accountId}")
    public ResponseEntity<AccountDTO> getAccount(@PathVariable Integer accountId) {
        AccountDTO accountDTO = new AccountDTO();
        accountDTO.setId(accountId);
        accountDTO.setName("name");
        return new ResponseEntity<>(accountDTO, HttpStatus.OK);
    }
}
