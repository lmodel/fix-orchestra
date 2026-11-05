package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One connection between two parties, with the identifiers, role, activation times and security keys that set it up.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraSessionV10 extends OrchestraBaseInterfaceV10 {

  private List<OrchestraSessionIdentifierV10> fixiIdentifier;
  private String fixiActivationTime;
  private String fixiDeactivationTime;
  private String fixiRole;
  private String fixiSecurityKeys;


}