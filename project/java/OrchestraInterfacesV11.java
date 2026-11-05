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
  A description of the services and sessions a party offers and how to reach them, headed by its Dublin Core metadata.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraInterfacesV11  {

  private OrchestraMetadata fixiMetadata;
  private List<OrchestraInterfaceV11> fixiInterface;


}