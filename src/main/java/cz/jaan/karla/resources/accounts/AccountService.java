package cz.jaan.karla.resources.accounts;

import cz.jaan.karla.resources.accounts.DTO.AccountDTO;
import cz.jaan.karla.resources.accounts.DTO.CreateAccountDTO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class AccountService {

    @Autowired
    private AccountRepository accountRepository;

    // GET /accounts
    public List<AccountDTO> getAccounts() {
        Iterable<Account> accounts = accountRepository.findAll();
        return toDTOList(accounts);
    }

    // GET /accounts/{accountId}
    public AccountDTO getAccount(Integer accountId) {
        Account account = accountRepository.findById(accountId).orElseThrow();
        return new AccountDTO(account);
    }

    // POST /accounts/create
    public AccountDTO postCreateAccount(CreateAccountDTO createAccountDTO) {
        Account account = new Account();
        account.setName(createAccountDTO.getName());
        account = accountRepository.save(account);
        return new AccountDTO(account);
    }

    private List<AccountDTO> toDTOList(Iterable<Account> accounts) {
        List<AccountDTO> accountDTOS = new ArrayList<>();
        for (Account account : accounts)
            accountDTOS.add(new AccountDTO(account));
        return accountDTOS;
    }

}
