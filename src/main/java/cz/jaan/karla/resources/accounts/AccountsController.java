package cz.jaan.karla.resources.accounts;

import cz.jaan.karla.resources.GenericDTO;
import cz.jaan.karla.resources.accounts.DTO.AccountDTO;
import cz.jaan.karla.resources.accounts.DTO.CreateAccountDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.context.request.async.DeferredResult;

import java.io.IOException;
import java.util.List;

import static java.lang.String.format;

@RestController
public class AccountsController {

    @Autowired
    private AccountService accountService;

    @GetMapping("/accounts")
    public @ResponseBody List<AccountDTO> accounts() {
        return accountService.getAccounts();
    }

    @GetMapping("/bin/accounts")
    public @ResponseBody byte[] accountsBin() throws IOException {
        List<AccountDTO> accountDTOS = accountService.getAccounts();
        return GenericDTO.listDTOsToBytes(accountDTOS);
    }

    @PostMapping("/accounts/create")
    public @ResponseBody AccountDTO createAccount(@RequestBody CreateAccountDTO payload) {
        return accountService.postCreateAccount(payload);
    }

    @GetMapping("/accounts/{accountId}")
    public @ResponseBody AccountDTO getAccount(@PathVariable Integer accountId) {
        return accountService.getAccount(accountId);
    }
}
