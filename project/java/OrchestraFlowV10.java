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
  A one-way flow of messages from one actor to another, with its delivery guarantee.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraFlowV10  {

  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrName;
  private String fixrSource;
  private String fixrDestination;
  private String fixrReliability;


}