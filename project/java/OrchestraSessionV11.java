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
public class OrchestraSessionV11 extends OrchestraBaseInterfaceV11 {

  private List<OrchestraSessionIdentifierV11> fixiIdentifier;
  private String fixiRole;
  private String fixiSecurityKeys;
  private String fixiActivationTime;
  private String fixiDeactivationTime;


}